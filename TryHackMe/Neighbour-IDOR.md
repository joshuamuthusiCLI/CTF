# TryHackMe — Neighbour

## Overview

Neighbour is a TryHackMe web application security challenge focused on
Insecure Direct Object Reference (IDOR).

The objective was to access another user's profile and retrieve the flag.

**Target:** `10.48.162.65`

---

## Enumeration

I started by navigating to the target:

```text
http://10.48.162.65

The application presented a login page containing the following message:

Don't have an account? Use the guest account! (Ctrl+U)

This suggested that the page source might contain useful information.

I opened the page source using:

Ctrl + U

The HTML source contained the following comment:

<!-- use guest:guest credentials until registration is fixed.
"admin" user account is off limits!!!!! -->

This revealed the guest credentials:

Username: guest
Password: guest

The comment also confirmed the existence of an admin account.

**Authentication**

I logged into the application using:

Username: guest
Password: guest

After authentication, the application displayed:

Hi, guest. Welcome to our site.
Try not to peep your neighbor's profile.

This provided another hint toward accessing another user's profile.

**Vulnerability Discovery
**
After logging in, I examined the profile URL:

http://10.48.162.65/profile.php?user=guest

The important parameter was:

user=guest

The application appeared to use the username supplied in the URL to determine
which profile should be displayed.

Since the username was controlled by the client, I tested whether changing it
would allow access to another user's profile.

**Exploitation**

I modified:

/profile.php?user=guest

to:

/profile.php?user=admin

The resulting request was:

http://10.48.162.65/profile.php?user=admin

The application returned the administrator's profile without requiring
additional authorization.

This confirmed the presence of an IDOR vulnerability.

Flag

The administrator's profile contained the flag: -- as displayed in your browser

**Vulnerability Analysis
**
The application trusted the user parameter supplied by the client without
performing an appropriate server-side authorization check.

An authenticated guest user was therefore able to change:

user=guest

to:

user=admin

and access another user's information.

This is an example of Insecure Direct Object Reference (IDOR).

**Impact**

An IDOR vulnerability can allow unauthorized users to access information
belonging to other users.

Depending on the application, this could expose:

**Remediation
**
The application should perform authorization checks on the server before
returning any requested resource.

The server should:

Authenticate the requesting user.
Identify the requested resource.
Verify that the user is authorized to access it.
Return the resource only after authorization succeeds.

Client-controlled parameters should never be treated as proof of authorization.
User profiles
Personal information
Private documents
Account information
Administrative data
Other sensitive resources
