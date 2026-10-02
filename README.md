# cornercase

**A reaction-wheel cube that balances on its corner.**

> 🚧 Work in progress — started October 2026. See the [roadmap](#roadmap) for current status.

`cornercase` is a self-balancing cube driven by three reaction wheels. It is built from the ground up: a custom FOC motor driver on an STM32G474, IMU-based state estimation, and LQR control. The same system is also controlled by a reinforcement-learning policy trained in MuJoCo and deployed on the microcontroller, so the two approaches can be compared on real hardware.

The project grows in stages: first balancing on an edge (1D), then on a corner (3D), and finally standing up on its own (swing-up).

## Goals

- **Control:** Derive the dynamics, linearize around the upright equilibrium, and stabilize with LQR.
- **Estimation:** Estimate attitude from a 6-axis IMU using a complementary filter and an EKF, compared on the same data.
- **Embedded:** Field-oriented control of gimbal BLDC motors on an STM32G474 with a custom three-channel driver PCB.
- **Learning:** Train a balancing policy in MuJoCo with domain randomization, quantize it, and run it on the MCU inside the control loop.
- **Sim-to-real:** Quantify how well simulation predicts hardware behavior, and compare LQR and RL under identical disturbance tests.

## Repository layout

```
cornercase/
├── models/     # MuJoCo MJCF models (1D pendulum, 3D cube)
├── sim/        # Python: dynamics, LQR design, simulation, RL training
├── docs/       # Derivations, notes, test reports
└── firmware/   # STM32G474 firmware (FOC, estimation, control, telemetry)
```

## Getting started (simulation)

Requires Python 3.10+.

```bash
git clone https://github.com/<user>/cornercase.git
cd cornercase
python3 -m venv .venv
source .venv/bin/activate
pip install mujoco numpy scipy sympy matplotlib control
```

Check that the MuJoCo viewer opens:

```bash
python -m mujoco.viewer
```

> **macOS note:** Scripts that use the passive viewer (`mujoco.viewer.launch_passive`) must be run with `mjpython` instead of `python`.

## Hardware (planned)

| Part | Role |
| --- | --- |
| STM32G474 (NUCLEO-G474RE for prototyping) | Control, estimation, FOC |
| Gimbal BLDC motors with encoders ×3 | Reaction wheel actuation |
| 6-axis IMU | Attitude estimation |
| Custom 3-channel FOC driver PCB (KiCad) | Motor drive, current sensing, power |

The final bill of materials will be added once the parts are chosen and tested.

## Roadmap

- [ ] **Oct 2026** — 1D dynamics (Lagrange), MuJoCo model, LQR in simulation
- [ ] **Nov 2026** — FOC current/velocity loops on the STM32G474
- [ ] **Dec 2026** — IMU integration, complementary filter vs. EKF, telemetry tool, CI and unit tests
- [ ] **Jan 2027** — 1D prototype mechanics
- [ ] **Feb 2027** — 1D balancing on hardware
- [ ] **Mar 2027** — Custom driver PCB (rev A)
- [ ] **Apr 2027** — 3D cube model and LQR in simulation
- [ ] **May 2027** — Corner balancing on hardware
- [ ] **Jun 2027** — RL policy training with domain randomization
- [ ] **Jul 2027** — Policy deployment on the MCU, LQR vs. RL comparison
- [ ] **Aug 2027** — ROS 2 telemetry bridge, swing-up (stretch goal), final report and video

## Results

Results, plots and videos will be added here as each milestone is completed.

## License

This project is licensed under the [MIT License](LICENSE).