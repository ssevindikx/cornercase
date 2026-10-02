import time
import mujoco
import mujoco.viewer

m = mujoco.MjModel.from_xml_path("models/pendulum.xml")
d = mujoco.MjData(m)
d.qpos[0] = 0.05

with mujoco.viewer.launch_passive(m, d) as v:
    while v.is_running():
        t0 = time.time()
        d.ctrl[0] = -20 * d.qpos[0] - 2 * d.qvel[0]
        mujoco.mj_step(m, d)
        v.sync()
        dt = m.opt.timestep - (time.time() - t0)
        if dt > 0:
            time.sleep(dt)
