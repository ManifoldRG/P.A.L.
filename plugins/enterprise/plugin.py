from ..proactive_plugin import ProactivePlugin

class EnterprisePlugin(ProactivePlugin):
    def __init__(self):
        self.user_activity = "A customer searches for a white colored sectional sofa, and scrolls through the results in 5 seconds.\nThey modify the search to a white colored U-shaped sectional. \nThey click on the Radley 5-piece Fabric Chaise Sectional Sofa from the results. \nThey stay on the page for 5 minutes, and click on the different view options, 2 times on each view option. \nAt the time of this event, the Radley costs $2200 and is at a discounted price because of a limited-time special. \nThis model is currently out of stock. "
        self.knowledge_base = "Couches similar to the Radley 5-piece Fabric Chaise Sectional sofa from Macy's: \n1. Jollene 113 2-Pc. Fabric Sectional: A stylish alternative with a sale price of $1,399.00 \n2. Radley 4-Pc. Fabric Chaise Sectional Sofa with Wedge Piece: This option offers a different configuration and is on sale for $2,049.00 \n3. Radley Fabric 5-Piece Sectional Sofa: Another choice with a sale price of $2,139.00"
    
    def invoke(self, event):
        output = "Real-time customer activity on the website:\n"+self.user_activity+"\nKnowledge Base from the website:\n"+self.knowledge_base
        #print(output)
        return output
