# drf-social-network

<p> **This is simple DRF Social Network with basic implementation**<p>

<p>With following features:</p>
<p>Basic models:</p>
<ul>
<li>User</li>
<li>Post (always made by a user)</li>

</ul>

<p>Basic features:</p>
<ul>
<li>user signup</li>
<li>user login</li>
<li>post creation</li>
<li>post like</li>
<li>post unlike</li>
<li>analytics  about how many likes was made. Example url
/api/analytics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics
aggregated by day.</li>
<li>user activity an endpoint which will show when user was login last time and when he
mades a last request to the service.</li>
</ul>

<p>Token:</p>
<li>JWT</li>

<p>To install project type:</p>
```
pip install -r requirements.txt
```