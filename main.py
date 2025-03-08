from fastapi import FastAPI
import random

app= FastAPI()
# we will build two endpoints
side_hustles = [
    "Blogging - Writing and publishing content online to share knowledge and monetize through ads or sponsorships.",
    "Freelancing - Offering services independently to clients on a project or contract basis.",
    "Affiliate Marketing - Earning commissions by promoting and selling other companies' products or services.",
    "Online Courses - Creating and selling educational content through video lessons or written materials.",
    "Podcasting - Producing audio content on various topics and monetizing through ads or sponsorships.",
    "E-commerce - Selling physical or digital products through an online store",
    "Dropshipping - Selling products without holding inventory, as suppliers handle storage and shipping.",
    "Print on Demand - Selling custom-designed products printed only after an order is placed.",
    "Social Media Management - Managing and growing social media accounts for businesses or individuals.",
    "Web Development - Building and designing websites for clients or personal projects.",
    "App Development - Creating mobile applications for iOS or Android devices.",
    "SEO Consulting - Providing services to improve a website's search engine ranking and visibility.",
    "Virtual Assistant - Offering administrative, technical, or creative support remotely.",
    "Graphic Design - Creating visual content for print or digital media.",
    "Copywriting - Writing persuasive content for advertisements, websites, or marketing materials.",
    "Consulting - Providing expert advice and guidance on a specific topic or industry.",
    "Online Coaching - Offering personalized guidance and support to clients through virtual sessions.",
    "Public Speaking - Delivering speeches or presentations at events, conferences, or workshops.",
    "Event Planning - Organizing and coordinating events such as weddings, parties, or corporate functions.",
]
money_quotes = [
    "Money is a terrible master but an excellent servant.",
    "Money often costs too much.",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.",
    "Money is a guarantee that we may have what we want in the future. Though we need nothing at the moment it insures the possibility of satisfying a new desire when it arises.",
    "Money is like love; it kills slowly and painfully the one who withholds it, and enlivens the other who turns it on his fellow"
    "Money is a terrible master but an excellent servant.",
    "Money often costs too much.",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.",
    "Money is a guarantee that we may have what we want in the future. Though we need nothing at the moment it insures the possibility of satisfying a new desire when it arises.",
    "Money is like love; it kills slowly and painfully the one who withholds it, and enlivens the other who turns it on his fellow"
]
@app.get("/side-hustles")
def get_side_hustles(apikey: str):
   """Returns a random side hustle idea."""
   if apikey !="1234567890":
    return{"error": "Invalid API Key"}
   return{"side_hustle": random.choice(side_hustles)}

@app.get("/money-quotes")
def get_money_quotes(apikey: str):
   """Returns a random money quote."""
   if apikey !="1234567890":
     return{"error": "Invalid API Key"}
   return{"money_quote": random.choice(money_quotes)}

