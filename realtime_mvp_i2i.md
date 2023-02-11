# Ref

[Real-time Machine Learning For Recommendations](https://eugeneyan.com/writing/real-time-recommendations/)

Many US internet co. are still wondering if there's value in real-time ML. Chinese counterparts are already doing realtime inference + online training.

1. When does real-time recommendation make sense? When does not?
2. How have China and US companies implemented real-time recommenders?
3. How can we design and implement a simple MVP?

# When (not) to use real-time recommendations?

1. batch recommendations are computationally cheaper.
   1. generated once a day and benebit from batch processing's rconomies of scale
   2. served via a key-value lookup.
2. batch recommendations are also simpler ops-wise.
   1. decouple computation from serving - even if the compute stel fails. there's no customer -facing impact.
3. realtime recommendations ususally require more computation
   1. (aggregate streamed event (click, like, purchase and generate new recommendations on demand)
4. need low-latency high throughput API with 24/7 uptime.

# Why real-time recommendations then?

1. useful when the customer journey is mission-centric and depends on the context. (the mission is time-sensitive)
e.g.
   * shopping is a mission-centric activity. - if I usually shop for clothes, my u2i recommendations will mostly be fashion recommendations. However, if I need a new wide-screen monitor and start browsing for one, my u2i recommendations should update ASAP to help me quickly fulfill my mission (lest I go to a competing app).
     * in this scenario, batch recommendations don't react fast enough. even updated, there is a data imbalance issue.
   * movies we watch **depend on context**
     * long-term preferences are fairly stable.
     * whether we're along, with friend, with a romantic interest, or with children, also depend on our mood.
   * Travel(vacation destinations are often changing)
   * Youtube(we watch videos for coding, yoga, and recipes within the same day)
   * Serving ads(our interest is time-sensitive; our attention spans are shrinking)
2. when the majority of oyur customers are new. This happens when we're in the customer acquisition stage(just launch a new product or entered a new market)

# Example

Here’s how recommendations are updated and served. As the user browses on the app:

With each item interaction (e.g., click, like, add-to-cart, purchase)

ABFS computes user and item statistical features. These are passed to BE, and optionally updated in iGraph asynchronously.

BE generates the top 1,000 candidates based on user and item features (i.e., user preference, item trends) from ABFS. In the image, we see BE using the Swing i2i and c2i (category-to-item) algorithms.

RTP ranks the 1,000 candidates. 

Features can be added at this stage, such as user profile (gender, age, price propensity), item attributes (category, brand, seller), context (match with user last click/search), cross features (i.e., interaction features), and sequence features (click/category sequence). The top 600 products are presented to the user.


# Design and implement an MVP

* requirements (or constraints)
* methodology
* implementation

google - 500ms reduced traffic by 20%
amazon 100ms additional latancy reduce profit 1%

* latency : 200ms
* throughtput 1000 qps
* cost : achieve healthy ROI --> revenue --> infra budget. (10k US monthly)

* method : word2vec
* candidates : ANN
* ranking : logistic regression (beyond ranking metrics, business metrics is more important)
  * goal --> increased engagement
    * sell ads based on clicks.
    * ctr.
    * dau
  * goal --> customer acqusition (optimize first sell)
    * unit sold
    * conversion
    * mau
    * willness to take a hit on revenue.
  * goal --> revenue
    * revenue per session 
    * average basket size
    * customer lifetime value

* infra
  * EC2 instances (horizontally with a load balancer in the front)
    * 30 m5.xlarge 
      * 1200qps (throughput)
      * median latency 25ms, 99th 65ms
      * cost - 5.5k (within 10k budget)
  * simplify developement - AWS SageMaker.





