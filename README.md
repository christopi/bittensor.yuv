<div align="center">

# vidAIo Subnet
Revolutionizing Video Upscaling with AI-Driven Decentralization on the Bittensor Ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Bittensor](https://bittensor.com/whitepaper)  •  [Discord](https://discord.gg/9HDBfzTuJY)  • [App]()
</div>

## Introduction

### Our Mission
vidAIo's mission is to democratize video enhancement through decentralization, artificial intelligence, and blockchain technology. Leveraging the Bittensor ecosystem, vidAIo provides creators, businesses, and developers with scalable, affordable, and high-quality video upscaling solutions while ensuring full ownership and control over their content.

### Abstract
vidAIo addresses the growing demand for high-quality video content by introducing a decentralized, AI-driven video upscaling platform. Built on the Bittensor ecosystem, vidAIo disrupts traditional centralized solutions that are costly, resource-intensive, and inaccessible to many. By utilizing advanced AI and machine learning, vidAIo offers scalable, cost-effective, and high-quality video enhancement services.

## Subnet Architecture

### Overview
- **Miners**: Handle video upscaling tasks and optimize models to ensure high-quality outputs.
- **Validators**: Assess miner performance using predefined metrics to maintain network integrity.

### Miners
Miners enhance video quality using AI-driven upscaling techniques. They can:
- Optimize open-source models or develop proprietary ones for superior results.
- Handle video upscaling requests from validators and end-users.

### Validators
Validators ensure miners deliver consistent, high-quality results by evaluating performance through synthetic and organic queries.

### Synapses
#### Synthetic Query
Validators benchmark miner performance using controlled datasets:
- Input a 4K video and evaluate its score A using metrics like TOPIQ
- Downscale the 4K video to HD resolution
- Miners process the HD video and upscale it back to 4K
- Validators evaluate the upscaled output and assign it score B using metrics like TOPIQ
- Calculate the miner's performance by comparing score A and score B, factoring in latency

#### Organic Query
Real-world video data uploaded by users is processed as follows:
- Videos are chunked and queued for miners
- Miners process and upscale the chunks
- Results are aggregated and delivered back to users

## Subnet Incentive Mechanism
-
-
-
-
-
-

## Installation

#### [Miner Setup Guide](docs/miner_setup.md)

#### [Validator Setup Guide](docs/validator_setup.md)

### Latest release:
[Here is changelog](docs/changelog.md)

## Roadmap

### Phase 1: Implementing the Upscaling Synapse
- Launch the subnet with AI-powered video upscaling.
- Focus on real-time processing of low-quality videos into high-definition formats.

### Phase 2: Developing an AI-Powered Video Compression Model
- Build AI models for adaptive bitrate streaming.
- Optimize bandwidth usage while maintaining video quality.

### Phase 3: Implementing the Transcode Optimization Synapse
- Introduce AI-driven transcoding for compatibility across devices.
- Evaluate miners on speed, quality, and efficiency.

### Phase 4: On-Demand Streaming Architecture
- Enable decentralized on-demand video streaming with integrated storage.
- Utilize peer-to-peer (P2P) models for redundancy and high availability.

### Phase 5: Live Streaming Through the Subnet
- Introduce live streaming with real-time AI-powered upscaling and transcoding.
- Integrate adaptive bitrate streaming for smooth playback.

### Phase 6: Subnet API for Real-World Integration
- Develop a RESTful API for seamless integration with external platforms.
- Include features for uploading, processing, and retrieving videos.




## Appendix

### A. Technical Glossary
- **VMAF**: [Video Multimethod Assessment Fusion](https://github.com/Netflix/vmaf)
- **LPIPS**: [Learned Perceptual Image Patch Similarity](https://github.com/richzhang/PerceptualSimilarity)
- **TOPIQ**: [Top-down Image Quality Assessment](https://arxiv.org/pdf/2308.03060v1)
- **Bittensor Subnet**: [Decentralized AI Framework](https://docs.bittensor.com)