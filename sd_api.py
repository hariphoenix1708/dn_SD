import base64
import httpx


async def inpaint(image: bytes, mask: bytes) -> bytes:
    image = base64.b64encode(image).decode()
    mask = base64.b64encode(mask).decode()

    async with httpx.AsyncClient(timeout=None) as client:
        r = await client.post(
            "http://localhost:7861/sdapi/v1/img2img",
            json={
                "init_images": [image],
                "resize_mode": "1",
                "denoising_strength": 0.9,
                "mask": mask,
                "mask_blur": 8,
                "prompt": "fully nude fit girl, big perfect sexy breast, hyper detailed, intricate skin texture, (goosebumps:1.3)",
                "negative_prompt": "(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation",
                "steps": 26,
                "sampler_index": "Euler a",
                "inpaint_full_res": False,
            }
        )
    assert r.is_success

    result_image = r.json()["images"][0]
    return base64.b64decode(result_image)

