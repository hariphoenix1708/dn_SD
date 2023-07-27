from PIL import Image

#Import Neural Network Model
from .gan import DataLoader, DeepModel, tensor2im

#OpenCv Transform:
from .opencv_transform.dress_to_correct import create_correct
from .opencv_transform.mask_extracting import extract_mask

"""
run.py

This script manage the entire transormation.

Transformation happens in 6 phases:
    1: dress -> correct [opencv] dress_to_correct
    2: correct -> mask_in_img:  [GAN] correct_to_mask
    3: mask_in_img -> mask [opencv] extract_mask
"""

class Options():

    #Init options with default values
    def __init__(self):
    
        # experiment specifics
        self.norm = 'batch' #instance normalization or batch normalization
        self.use_dropout = False #use dropout for the generator
        self.data_type = 32 #Supported data type i.e. 8, 16, 32 bit

        # input/output sizes       
        self.batchSize = 1 #input batch size
        self.input_nc = 3 # of input image channels
        self.output_nc = 3 # of output image channels

        # for setting inputs
        self.serial_batches = True #if true, takes images in order to make batches, otherwise takes them randomly
        self.nThreads = 1 ## threads for loading data (???)
        self.max_dataset_size = 1 #Maximum number of samples allowed per dataset. If the dataset directory contains more than max_dataset_size, only a subset is loaded.
        
        # for generator
        self.netG = 'global' #selects model to use for netG
        self.ngf = 64 ## of gen filters in first conv layer
        self.n_downsample_global = 4 #number of downsampling layers in netG
        self.n_blocks_global = 9 #number of residual blocks in the global generator network
        self.n_blocks_local = 0 #number of residual blocks in the local enhancer network
        self.n_local_enhancers = 0 #number of local enhancers to use
        self.niter_fix_global = 0 #number of epochs that we only train the outmost local enhancer

        #Phase specific options
        self.checkpoints_dir = "checkpoints/cm.lib"
        self.dataroot = ""


# process(cv_img, mode)
# return:
# 	watermark image
def process(cv_img):

    #InMemory cv2 images:
    dress = cv_img
    correct = create_correct(dress)

    opt = Options()

    #Load Data
    data_loader = DataLoader(opt, correct)
    dataset = data_loader.load_data()
    data = next(iter(dataset))
            
    #Create Model
    model = DeepModel()
    model.initialize(opt)

    #Run for every image:
    generated = model.inference(data['label'], data['inst'])

    im = tensor2im(generated.data[0])

    mask = extract_mask(im)
    return Image.fromarray(mask)

