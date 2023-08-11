import base64
import httpx

async def inpaint(image: bytes, mask: bytes) -> bytes:
    image = base64.b64encode(image).decode()
    mask = base64.b64encode(mask).decode()

    async with httpx.AsyncClient(timeout=None) as client:
        r = await client.post(
            #"http://localhost:7861/sdapi/v1/img2img",
            #"comic-caribou-frankly.ngrok-free.app.localhost:7861/sdapi/v1/img2img",
            "https://9c3e-34-83-187-254.ngrok.io/sdapi/v1/img2img",
            json={
                "init_images": [image],
                "resize_mode": "1",
                "denoising_strength": 0.9,
                "mask": mask,
                "mask_blur": 8,
                #"prompt": "(nude girl, undress her, sexy body, sexy breasts), erect nipples, shaved pussy, detailed vagina, soft tighs, intricate skin texture, smooth skin, natural skin tone, realistic, nsfw, (goosebumps:1.3)",
                "prompt": "sexy girl, perfect body, nude, adaptive pose, (realistic), gorgeous , beautiful, thick thighs, nsfw, shaved pussy, harsh flash, Shading and Lighting, Radiosity, ray tracing, ray casting, texture mapping, sharpness, grain, shot on iphone 7, photorealistic, 4K, high-detail, RAW",
                #"prompt": "naked girl, bare naked, (make her nude, completely nude), nude girl, perfect sexy breast, midium breasts, highly detailed breasts, sexy body, shaved pussy, detailed vagina, soft tighs, intricate skin texture, (goosebumps:1.3)",
                #"prompt": "make her nude below face, completely nude, sexy girl, perfect sexy breast, perfect hands, realistic hands, extremely detailed hands, individual fingers, intricate fingers, 8k hands, perfect body, realistic body, extremely detailed body, 8k body hyper detailed, intricate skin texture, unreal engine, (goosebumps:1.3)",
                #"negative_prompt": "inpainting trace, border lines, (deformed, deformed body, distorted, disfigured:1.3), black border, poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, badhandv4, bad-artist, EasyNegativeV2, (low quality, worst quality)",
                "negative_prompt": "out of frame, two heads, totem pole, several faces, extra fingers, mutated hands, extra hands, extra feet, ribs, bones, muscular, muscular body, muscles, (poorly drawn hands:1.21), (poorly drawn face:1.21), (mutation:1.331), (deformed:1.331), (ugly:1.21), blurry, (bad anatomy:1.21), (bad proportions:1.331), (extra limbs:1.21), cloned face, (anime:1.331), (skinny:1.331), glitchy, saturated colors, distorted fingers, oversaturation, (penis:1.3), 3d, cartoon, low-res, text, error, cropped, worst quality, low quality, jpeg artifacts, duplicate, morbid, mutilated, out of frame ,extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, image compression, compression, noise, closeup, flat, cartoon, 3d,(disfigured), cgi, photoshop, (bad art), (deformed), (poorly drawn), (extra limbs), (close up),strange colors, blurry, boring, sketch, lackluster, cartoon, 3d, (disfigured), (bad art), (deformed), (poorly drawn), (extra limbs), (close up), strange colors, blurry, boring, sketch, lackluster, High pass filter,, ((out of focus body)), ((out of focus face)), ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), \[out of frame\], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)),(((missing feet))), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), ugly, man, (headshot:1.3), child, (closeup:1.3), fat, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, (deformed body:1.3)",
                "steps": 24,
                #"sampler_index": "DPM++ 2M Karras",
                #"sampler_index": "DPM++ 2M SDE Karras",
                "sampler_index": "Euler a",
                "inpaint_full_res": False,
            }
        )
    assert r.is_success

    result_image = r.json()["images"][0]
    return base64.b64decode(result_image)
