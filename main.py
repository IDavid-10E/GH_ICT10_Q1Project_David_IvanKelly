from pyscript import document

def show_summary(e):
    name = document.getElementById('Name').value
    address = document.getElementById('Address').value
    contact = document.getElementById('Contact').value

    total = 0.0
    items = []

    if document.getElementById('menu1').checked:
        total += 510
        items.append("Steak Pesto")

    if document.getElementById('menu2').checked:
        total += 1100
        items.append("Ribeye Steak")

    if document.getElementById('menu3').checked:
        total += 220
        items.append("Caprese Caesar Salad")

    if document.getElementById('menu4').checked:
        total += 96
        items.append("Lime Juice")

    if document.getElementById('menu5').checked:
        total += 45
        items.append("Perrier Sparkling Water")

    if document.getElementById('menu6').checked:
        total += 140
        items.append("Zero Sugar Fudge Brownie")

    summary = f"""
    Order for: {name}<br>
    Address: {address}<br>
    Contact number: {contact}<br>
    Items Ordered: {', '.join(items) if items else 'None'}<br>
    Total: ₱{total:.2f}
    """

    document.getElementById("summary").innerHTML = summary
