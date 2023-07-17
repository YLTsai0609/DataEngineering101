# ref

https://blog.cloud-ace.tw/identity-security/what-is-cloud-iam/

# IAM - 設計理念

Eric, 需要在 Compute Engine 取得 Compute Admin

Who (Identity)

Resource(Compute Engine)

Role (Do what) - (Compute Admin)

# IAM - 6大實體

# Identity (人、程式碼金鑰、群組, ...) (1)

被 Cloud IAM 授權的 Email 身份

1. Google Account - e.g. abcd@gmail.com
2. Service Account - usually for programming, - 提供應用程式在 GCP 上的權限
3. Google Group - **多個 Google Accounts / Service Accounts 的集合**
   1. 每個 Google Group 有唯一的電子郵件帳號
   2. 用途 : 透過一個帳號直接對集合當中的帳號進行授權或是權限的調整
   3. Google Group 無法作為 GCP 登入帳號

4. G Suite Domain： G Suite Domain 是整個代表著一整個創建在組織 G Suite 帳號下的虛擬群組，跟 Google Group 相同的地方是，G Suite Domain 方便管理員對群組帳號進行管理，但是 G Suite Domain 這個帳號本身同樣無法作為登入使用 GCP 的帳號。
5. Cloud Identity： 功能跟 G Suite Domain 類似， 差別是 Cloud Identity 可以讓沒有使⽤ G Suite 的企業或公司將⾃⼰的 Domain（如： example.com.tw） 註冊⾄ GCP 的 Organization，以便管理員在 Cloud IAM 管理 Domain 底下的帳號。關於 Cloud Identity Free 的帳號註冊教學，可以參考這篇文章。

# Resource(目標資源 - Compute Engine, BQ, xxx) (2)


# Permission(可對資源做什麼操作 - BQ, read, write, admin, rea session, ....) (3)

* pubsub.subscriptions.consume
* compute.instances.delete
* compute.instances.get
* compute.instances.start
* compute.instances.stop
* Permission 不會直接授權給使用者，而且給 Role， Role 像是多個 permission 的集合

# Roles (4)

* Basic Roles
  * Owner / Editor / Viewer
  * Pub/Sub Publisher

* Custom Roles
  * Editor 會包含若干個 permission，如果預設的 Roles，無辦法滿足，那麼就可以選擇 Custom Roles

# IAM Policy


# IAM Resource Hierarchy

Organization --> Folder --> Project --> Resource

可以設定 IAM Policy。資源層級有繼承性

Organization 的 Editor 最凍享有該 Organization 以下任何 Project 的 Editor 權限


# Ref

Role : Custom DSA-DE Role???
