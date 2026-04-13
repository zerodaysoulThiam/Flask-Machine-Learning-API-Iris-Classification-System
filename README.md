<!---------------------------------------------------------------------
  🔐 ABBLIX OIDC SERVER | PREMIUM README 
  ONE MAGICAL BLOCK — CERTIFIED OPENID CONNECT PROVIDER
---------------------------------------------------------------------->

<div align="center">

<!-- GLOW TITLE & BADGES GALORE -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=32&duration=3000&pause=500&color=512BD4&center=true&vCenter=true&width=700&lines=🔐+ABBLIX+OIDC+SERVER;🚀+CERTIFIED+OPENID+PROVIDER;✨+.NET+8+%2B+9+%2B+10" alt="Typing SVG" />

[![Abblix OIDC Server](https://resources.abblix.com/imgs/jpg/abblix-oidc-server-github-banner.jpg)](https://www.abblix.com/abblix-oidc-server)

<p>
  <b>⚡ Production-ready OAuth2 & OpenID Connect Server for .NET</b><br>
  Certified • Secure • Modular • Free for non-commercial use
</p>

<!-- ========== SUPERNOVA BADGES SECTION (NO SEPARATION) ========== -->
<p align="center">
  <img src="https://img.shields.io/badge/.NET-8.0%2C%209.0%2C%2010.0-512BD4?style=for-the-badge&logo=dotnet" />
  <img src="https://img.shields.io/badge/language-C%23-239120?style=for-the-badge&logo=csharp" />
  <img src="https://img.shields.io/badge/OS-linux%2C%20windows%2C%20macOS-0078D4?style=for-the-badge&logo=windows" />
  <img src="https://img.shields.io/badge/CPU-x86%2C%20x64%2C%20ARM%2C%20ARM64-FF8C00?style=for-the-badge" />
  <img src="https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=security_rating&style=for-the-badge" />
  <img src="https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=reliability_rating&style=for-the-badge" />
  <img src="https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=sqale_rating&style=for-the-badge" />
  <img src="https://img.shields.io/badge/tests-2000%2B%20passing-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/github/v/release/Abblix/Oidc.Server?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/badge/OpenID%20Certified-634%2F634%20PASSED-00A859?style=for-the-badge&logo=openid" />
  <img src="https://img.shields.io/badge/license-Source%20Available-9400D3?style=for-the-badge" />
  <img src="https://img.shields.io/badge/free_for_non_commercial_use-brightgreen?style=for-the-badge" />
</p>

⭐ Star us on GitHub — your support motivates us a lot! 🙏😊

<p align="center">
  <a href="https://x.com/intent/tweet?text=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Abblix/Oidc.Server%20%23OpenIDConnect%20%23Security%20%23Authentication"><img src="https://img.shields.io/badge/share-000000?style=for-the-badge&logo=x&logoColor=white" /></a>
  <a href="https://www.facebook.com/sharer/sharer.php?u=https://github.com/Abblix/Oidc.Server"><img src="https://img.shields.io/badge/share-1877F2?style=for-the-badge&logo=facebook&logoColor=white" /></a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/Abblix/Oidc.Server"><img src="https://img.shields.io/badge/share-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://www.reddit.com/submit?title=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Abblix/Oidc.Server"><img src="https://img.shields.io/badge/share-FF4500?style=for-the-badge&logo=reddit&logoColor=white" /></a>
  <a href="https://t.me/share/url?url=https://github.com/Abblix/Oidc.Server&text=Check%20out%20this%20project%20on%20GitHub"><img src="https://img.shields.io/badge/share-0088CC?style=for-the-badge&logo=telegram&logoColor=white" /></a>
</p>

🔥 Why OIDC Server is the best choice for authentication — find out in our <a href="https://resources.abblix.com/pdf/abblix-oidc-server-presentation-eng.pdf">📑 presentation</a>

<!-- ANIMATED DIVIDER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=header&text=✨%20Certified%20OpenID%20Provider%20✨&fontSize=30&fontAlignY=40" width="100%" />

</div>

## 🚀 **About** — *Enterprise-grade OAuth2 & OIDC Server*

**Abblix OIDC Server** is a .NET library designed to provide comprehensive support for OAuth2 and OpenID Connect on the server side. It adheres to high standards of flexibility, reusability, and reliability, utilizing well-known software design patterns, including modular and hexagonal architectures. These patterns ensure the following benefits:

- **Modularity**: Different parts of the library can function independently, enhancing the library's modularity and allowing for easier maintenance and updates.
- **Testability**: Improved separation of concerns makes the code more testable.
- **Maintainability**: Clear structure and separation facilitate better management of the codebase.

The library also supports Dependency Injection through the standard .NET DI container, aiding in the organization and management of code. Specifically tailored for seamless integration with ASP.NET WebApi, Abblix OIDC Server employs standard controller classes, binding, and routing mechanisms, simplifying the integration of OpenID Connect into your services.

---

## 💎 **Abblix Account** — *Cloud-ready authentication service*

> **Abblix Account** is a ready-to-use service hosted in the cloud, built on this library. You get passkeys, MFA, social login, and security event notifications — everything your users need, integrated into your website in minutes.

👉 **See it live:** [Quorvel Coffee](https://quorvel.abblix.com) is a demo application using Abblix Account for user authentication. It shows how sign-in flows, session management, and user self-service — all delivered by Abblix Account — fit into a client website.

---

## ✨ **What's New** — *Version 2.2 (Latest)*

🚀 **Features**
- **Custom JWT Implementation**: Complete JWT signing/encryption infrastructure replacing `Microsoft.IdentityModel.Tokens` — uses `System.Text.Json.Nodes` and .NET crypto primitives directly
- **Enhanced JWE Algorithms**: `RSA-OAEP-256`, AES-GCM key wrapping (`A128GCMKW`/`A192GCMKW`/`A256GCMKW`), and direct key agreement (`dir`)
- **ACR/AMR Compliance (RFC 8176)**: Authentication Context Class Reference values in discovery and RFC 8176 Authentication Method References
- **CSP Nonce Support**: Template-based front-channel logout and check session iframe compatible with strict Content Security Policies

✏️ **Improvements**
- Configurable session cookie path in OIDC Session Management
- Operation capability validation for `JsonWebKey` classes
- Bidirectional interoperability tests with `Microsoft.IdentityModel.Tokens`

> See 📋[Release Notes](https://github.com/Abblix/Oidc.Server/releases/tag/v2.2) for full details.

---

## 🎓 **Certification** — *100% OpenID Foundation Certified*

<div align="center">
  <img src="https://resources.abblix.com/imgs/svg/abblix-oidc-server-openid-foundation-certification-mark.svg" width="120" />
</div>

We are certified in all profiles. During the certification process, we skipped ZERO tests and received NO warnings. All **634** tests ![Passed](https://img.shields.io/badge/PASSED-brightgreen). We are extremely proud of this achievement. It reflects our overall approach to any endeavor.

### Regular Profiles

| OIDC Profile | Response Types | Tests |
|--------------|----------------|-------|
| Basic OP | `code` | 36 |
| Implicit OP | `id_token` | 58 |
| Hybrid OP | `code id_token` | 102 |
| Config OP | `config` | 1 |
| Dynamic OP | `code` \| `code id_token` \| `code id_token token` \| `code token` \| `id_token` \| `id_token token` | 127 |
| Form Post OP | `basic` \| `implicit` \| `hybrid` | 196 |
| 3rd Party-Init OP | `code` \| `code id_token` \| `code id_token token` \| `code token` \| `id_token` \| `id_token token` | 12 |
| **Total** | | **532** |

### Logout Profiles

| OIDC Profile | Tests |
|--------------|-------|
| RP-Initiated OP | 66 |
| Session OP | 12 |
| Front-Channel OP | 12 |
| Back-Channel OP | 12 |
| **Total** | **102** |

---

## 📝 **How to Build** — *One command to rule them all*

```bash
# Open a terminal (Command Prompt, PowerShell, or Terminal)

# Clone the repository
git clone https://github.com/Abblix/Oidc.Server.git

# Navigate to the project directory
cd Oidc.Server

# Check if .NET SDK is installed
dotnet --version

# Restore dependencies
dotnet restore

# Compile the project
dotnet build
