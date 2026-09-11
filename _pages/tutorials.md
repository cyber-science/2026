---
title: Tutorial
layout: sub
permalink: /tutorial/
---
<h3>Tutorial</h3>
<hr/>

<style>
@media (max-width: 576px) {
  .tutorial-speaker-photo {
    float: none !important;
    display: block;
    margin: 0 auto 1rem;
  }
}
</style>

<h4>Resilient Delivery Pipelines: A Hands-On Kubernetes Tutorial on A/B Deployment, CI/CD Automation, and Observability-Driven Operations</h4>
<h5>Tutorial Time: TBD (3 hours)</h5>
<img src="{{ '/assets/images/tutorial_speaker/tony_de_souza-daw.jpg' | relative_url }}" class="tutorial-speaker-photo" align="left" style="border:10px solid white" width="200">
<h5><b>Dr Tony de Souza-Daw</b></h5>
<h6>
La Trobe University, Australia
</h6>
<p style="text-align: justify;">
<b>Abstract: </b>
Modern cyber-physical and cyber-social systems increasingly rely on Kubernetes for continuous delivery, resilience, and observability, yet these capabilities are often taught separately. This hands-on tutorial provides participants with an integrated, production-representative environment for building and operating a resilient Kubernetes delivery pipeline.
</p>
<p style="text-align: justify;">
Across three connected modules, participants first deploy two versions of a containerized Python web application and implement A/B traffic splitting, self-healing, and automated promotion to explore progressive delivery. They then provision a Kubernetes-native Jenkins CI/CD environment with persistent configuration and dynamic build agents to automate application deployment. Finally, participants implement full-stack observability using Prometheus, Grafana Alloy, Loki, and Grafana, and use controlled chaos scenarios to examine how operational incidents appear across alerts, metrics, and logs.
</p>
<p style="text-align: justify;">
Together, the modules form a continuous workflow from Git and Jenkins through Kubernetes deployment and A/B testing to end-to-end observability. Participants leave with practical experience and a reusable reference architecture illustrating how modern DevOps and Site Reliability Engineering practices can support resilient, observable cyber-infrastructure. The entire environment runs locally using VirtualBox virtual machines, requiring no cloud account or external Kubernetes cluster.
</p>
<p style="text-align: justify;">
<b>Biography: </b>
Tony de Souza-Daw is a Lecturer in Computer Science and Information Technology at La Trobe University, Australia. His research spans cybersecurity, cloud and distributed computing, runtime behaviour analysis, and applied data science, with recent work covering malware and botnet detection, big data security in supply chains, and machine learning applications in security and networked systems. He has authored numerous publications in international journals and conferences on information security and computing systems and brings extensive hands-on teaching experience in networking, systems, and applied computing to this tutorial.
</p>
<p style="text-align: justify;">
<b>Requirements: </b>
Participants will need to bring their own laptop, with at least 30 GB free disk space and virtualization support enabled in BIOS/UEFI; VirtualBox installed; VS Code installed; a GitHub account (used for the CI/CD module's Git repository and Jenkins pipeline trigger); Docker and kubectl inside the VM image. Stable internet is only needed for initial image/plugin downloads, not during the exercises themselves.
</p>
<hr/>

<h4>Full-Duplex Spoken Dialogue for Embodied AI: Applications in Virtual Avatars and Humanoid Robot Simulation</h4>
<h5>Tutorial Time: TBD (90 minutes; hybrid: on-site and online)</h5>
<img src="{{ '/assets/images/tutorial_speaker/ao_guo.jpg' | relative_url }}" alt="Dr Ao Guo" class="tutorial-speaker-photo" align="left" style="border:10px solid white" width="200">
<h5><b>Dr Ao Guo</b></h5>
<h6>
Assistant Professor, Department of Intelligent Systems<br/>
Graduate School of Informatics, Nagoya University, Japan
</h6>
<p style="text-align: justify;">
<b>Abstract: </b>
Spoken dialogue is becoming the primary interface to agents that have a body: virtual avatars in applications and games, and humanoid robots in shops, museums and homes.
</p>
<p style="text-align: justify;">
The technology itself has also moved quickly, from turn-based pipelines that wait for silence to full-duplex models that listen and speak at once, reproducing the overlap and backchannelling of human conversation. This tutorial offers a practical route through both. The first part introduces the development of spoken dialogue systems: the classical pipeline, incremental processing, turn-taking prediction, and current full-duplex models.
</p>
<p style="text-align: justify;">
The second part makes this concrete by connecting a dialogue system to a body: a virtual avatar and a simulated humanoid robot, in which speech, gesture and movement can be observed together and modified directly. Current work on connecting external actions to full-duplex models will be noted briefly, though it lies outside the main scope of the tutorial.
</p>
<p style="text-align: justify;">
Through this tutorial, participants will learn how modern spoken dialogue systems are structured, how full-duplex interaction differs from turn-based interaction, and what is involved in driving a virtual avatar and a simulated humanoid robot from a dialogue system.
</p>
<hr/>
