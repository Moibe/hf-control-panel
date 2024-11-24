from huggingface_hub import HfApi, SpaceHardware
import bridges
import time 

# Space will need your token to request hardware: set it as a Secret !
HF_TOKEN = bridges.hug
# Space own repo_id
repo_id = "Moibe/InstantID2"
api = HfApi(token=HF_TOKEN)


#runtime = api.get_space_runtime(repo_id=repo_id)
# print(runtime.stage)
# #"RUNNING_BUILDING"
# print(runtime.hardware)
# # #"cpu-basic"
# print(runtime.requested_hardware)
# # #"t4-medium"
#print(runtime.raw)

# # Pause your Space to avoid getting billed
# api.pause_space(repo_id=repo_id)
# # (...)
# # Restart it when you need it
# time.sleep(5)
# api.restart_space(repo_id=repo_id)

#api.request_space_hardware(repo_id=repo_id, hardware=SpaceHardware.ZERO_A10G)

# resultado = api.get_token_permission(bridges.hug)
# print(resultado)

# print(api.get_user_overview("Moibe"))

# print(api.space_info(repo_id))

print(api.whoami(bridges.hug))