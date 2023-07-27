import base64
import httpx


async def inpaint(image: bytes, mask: bytes) -> bytes:
    image = base64.b64encode(image).decode()
    mask = base64.b64encode(mask).decode()

    async with httpx.AsyncClient(timeout=None) as client:
        r = await client.post(
            #"http://localhost:7861/sdapi/v1/img2img",
            "https://02d4-34-32-133-227.ngrok.io/sdapi/v1/img2img",
            json={
                "init_images": [image],
                "resize_mode": "1",
                "denoising_strength": 0.9,
                "mask": mask,
                "mask_blur": 8,
                "prompt": "make her nude below face, completely nude, sexy girl, perfect sexy breast, perfect hands, realistic hands, extremely detailed hands, individual fingers, intricate fingers, 8k hands, perfect body, realistic body, extremely detailed body, 8k body hyper detailed, intricate skin texture, unreal engine, (goosebumps:1.3)",
                "negative_prompt": "deformed eyes, deformed face, deformed iris, deformed pupils, semi-realistic, Asian-Less-Neg, canvas frame, cartoon, 3d, loli, petite, child, infant, toddlers, chibi, (sd character:1.1), ((disfigured)), ((bad art)), ((deformed)),((extra limbs)),((close up)),((b&w)), blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), Photoshop, video game, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, 3d render, (tiara), (crown), (badhands), half body image, upper shot, half-body shot",
                "steps": 30,
                "sampler_index": "Euler a",
                "inpaint_full_res": False,
            }
        )
    assert r.is_success

    result_image = r.json()["images"][0]
    return base64.b64decode(result_image)

