import base64
import httpx


async def inpaint(image: bytes, mask: bytes) -> bytes:
    image = base64.b64encode(image).decode()
    mask = base64.b64encode(mask).decode()

    async with httpx.AsyncClient(timeout=None) as client:
        r = await client.post(
            #"http://localhost:7861/sdapi/v1/img2img",
            "https://comic-caribou-frankly.ngrok-free.app/sdapi/v1/img2img",
            json={
                "init_images": [image],
                "resize_mode": "1",
                "denoising_strength": 0.9,
                "mask": mask,
                "mask_blur": 8,
                "prompt": "(nude girl, undress her, sexy body, sexy breasts), erect nipples, shaved pussy, detailed vagina, soft tighs, intricate skin texture, smooth skin, natural skin tone, realistic, nsfw, (goosebumps:1.3)",
                #"prompt": "naked girl, bare naked, (make her nude, completely nude), nude girl, perfect sexy breast, midium breasts, highly detailed breasts, sexy body, shaved pussy, detailed vagina, soft tighs, intricate skin texture, (goosebumps:1.3)",
                #"prompt": "make her nude below face, completely nude, sexy girl, perfect sexy breast, perfect hands, realistic hands, extremely detailed hands, individual fingers, intricate fingers, 8k hands, perfect body, realistic body, extremely detailed body, 8k body hyper detailed, intricate skin texture, unreal engine, (goosebumps:1.3)",
                "negative_prompt": "inpainting trace, border lines, (deformed, deformed body, distorted, disfigured:1.3), black border, poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, badhandv4, (low quality, worst quality)",
                "steps": 24,
                "sampler_index": "DPM++ 2M Karras",
                #"sampler_index": "DPM++ 2M SDE Karras",
                #"sampler_index": "Euler a",
                "inpaint_full_res": False,
            }
        )
    assert r.is_success

    result_image = r.json()["images"][0]
    return base64.b64decode(result_image)
