from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)






@app.route('/')
def index():
    title = "Flask Travel"
    subtitle = "Для відпочинку"
    description = "Найпопулярніші напрямки "
    departures = {"kuiv": " з Києва", "lviw": " зі Львова", "odessa": " з Одеси", "chernivtsi": " з Чернівець",
                  "chernigiv": " з Чернігова"}

    tours = {
        1: {
            "title": "Закарпаття",
            "description": "затишний готель.",
            "departure": "kuiv",
            "picture": "https://zahidkurort.com.ua/wp-content/themes/kurort/cache/45/03cd84cf64a6145_1013x532.jpg",
            "price": 62000,
            "stars": "4",
            "country": "Пилипець",
            "nights": 6,
            "date": "2 березня",
        },
        2: {
            "title": "Батяр",
            "description": "Будинок готелю має форму короткої літери U. ",
            "departure": "lviw",
            "picture": "https://bukovel-hotel-ua.hotelmix.com.ua/data/Photos/OriginalPhoto/11709/1170996/1170996471/Bukovel-Hotel-Exterior.JPEG",
            "price": 85000,
            "stars": "5",
            "country": "Буковель",
            "nights": 8,
            "date": "12 січня",
        },
        3: {
            "title": "Ліжник",
            "description": "Готель з білого каменю",
            "departure": "odessa",
            "picture": "https://cf.bstatic.com/xdata/images/hotel/max500/266741392.jpg?k=8ca8f1ce6b54ff7d7bc5316c82f3d15aada16834b1b1108d8e79edca5d60c7b5&o=&hp=1",
            "price": 63000,
            "stars": "3",
            "country": "Косів",
            "nights": 11,
            "date": "7 лютого",
        },
        4: {
            "title": "Ведмежа",
            "description": "Красивий краєвид з вікна",
            "departure": "kuiv",
            "picture": "https://karpatskyi-teremok-dzembronia.hotelmix.com.ua/data/Photos/OriginalPhoto/12654/1265492/1265492017/Karpatskyi-Teremok-Exterior.JPEG",
            "price": 62000,
            "stars": "4",
            "country": "Космач",
            "nights": 9,
            "date": "22 жовтня",
        },
        5: {
            "title": "Сова",
            "description": "Розкішні апартаменти на березі водосховища",
            "departure": "chernivtsi",
            "picture": "https://pravda.if.ua/wp-content/uploads/2020/04/10827878_1539108119699451_4179360364797503328_o.jpg",
            "price": 68000,
            "stars": "4",
            "country": "Бакота",
            "nights": 8,
            "date": "18 вересня",
        },
        6: {
            "title": "Верховина",
            "description": "в центрі міста",
            "departure": "chernigiv",
            "picture": "https://static.karpaty.ua/uploads/house/55cc5c27c0557c2ebc003185/main_photo/big.jpg",
            "price": 53000,
            "stars": "3",
            "country": "Синевір",
            "nights": 13,
            "date": "15 серпня",
        },
        7: {
            "title": "Піп-Іван",
            "description": "З готелю близько до Чорногори",
            "departure": "odessa",
            "picture": "https://q-xx.bstatic.com/xdata/images/hotel/max500/300980475.jpg?k=a26871869739483c09ac4493f59c337ec2bc8acc5acd96d1b141b0f184399734&o=",
            "price": 72000,
            "stars": "5",
            "country": "Дземброня",
            "nights": 9,
            "date": "22 липня",
        },
        8: {
            "title": "Купель",
            "description": "термальні води",
            "departure": "kuiv",
            "picture": "https://turua.com.ua/upload/iblock/b6d/b6d7e9601f754931b633b8be6e10afd3.jpg",
            "price": 44000,
            "stars": "4",
            "country": "Велятино",
            "nights": 7,
            "date": "21 січня",
        },

    }

    @app.route('/departures/<departure>/')
    def filtered_departures(departure):
        departures = {"kuiv": " з Києва", "lviw": " зі Львова", "odessa": " з Одеси", "chernivtsi": " з Чернівець",
                      "chernigiv": " з Чернігова"}

        tours = {
            1: {
                "title": "Закарпаття",
                "description": "затишний готель.",
                "departure": "kuiv",
                "picture": "https://zahidkurort.com.ua/wp-content/themes/kurort/cache/45/03cd84cf64a6145_1013x532.jpg",
                "price": 62000,
                "stars": "4",
                "country": "Пилипець",
                "nights": 6,
                "date": "2 березня",
            },
            2: {
                "title": "Батяр",
                "description": "Будинок готелю має форму короткої літери U. ",
                "departure": "lviw",
                "picture": "https://bukovel-hotel-ua.hotelmix.com.ua/data/Photos/OriginalPhoto/11709/1170996/1170996471/Bukovel-Hotel-Exterior.JPEG",
                "price": 85000,
                "stars": "5",
                "country": "Буковель",
                "nights": 8,
                "date": "12 січня",
            },
            3: {
                "title": "Ліжник",
                "description": "Готель з білого каменю",
                "departure": "odessa",
                "picture": "https://cf.bstatic.com/xdata/images/hotel/max500/266741392.jpg?k=8ca8f1ce6b54ff7d7bc5316c82f3d15aada16834b1b1108d8e79edca5d60c7b5&o=&hp=1",
                "price": 63000,
                "stars": "3",
                "country": "Косів",
                "nights": 11,
                "date": "7 лютого",
            },
            4: {
                "title": "Ведмежа",
                "description": "Красивий краєвид з вікна",
                "departure": "kuiv",
                "picture": "https://karpatskyi-teremok-dzembronia.hotelmix.com.ua/data/Photos/OriginalPhoto/12654/1265492/1265492017/Karpatskyi-Teremok-Exterior.JPEG",
                "price": 62000,
                "stars": "4",
                "country": "Космач",
                "nights": 9,
                "date": "22 жовтня",
            },
            5: {
                "title": "Сова",
                "description": "Розкішні апартаменти на березі водосховища",
                "departure": "chernivtsi",
                "picture": "https://pravda.if.ua/wp-content/uploads/2020/04/10827878_1539108119699451_4179360364797503328_o.jpg",
                "price": 68000,
                "stars": "4",
                "country": "<Бакота>",
                "nights": 8,
                "date": "18 вересня",
            },
            6: {
                "title": "Верховина",
                "description": "в центрі міста",
                "departure": "chernigiv",
                "picture": "https://static.karpaty.ua/uploads/house/55cc5c27c0557c2ebc003185/main_photo/big.jpg",
                "price": 53000,
                "stars": "3",
                "country": "Синевір",
                "nights": 13,
                "date": "15 серпня",
            },
            7: {
                "title": "Піп-Іван",
                "description": "З готелю близько до Чорногори",
                "departure": "odessa",
                "picture": "https://q-xx.bstatic.com/xdata/images/hotel/max500/300980475.jpg?k=a26871869739483c09ac4493f59c337ec2bc8acc5acd96d1b141b0f184399734&o=",
                "price": 72000,
                "stars": "5",
                "country": "Дземброня",
                "nights": 9,
                "date": "22 липня",
            },
            8: {
                "title": "Купель",
                "description": "термальні води",
                "departure": "kuiv",
                "picture": "https://turua.com.ua/upload/iblock/b6d/b6d7e9601f754931b633b8be6e10afd3.jpg",
                "price": 44000,
                "stars": "4",
                "country": "Велятино",
                "nights": 7,
                "date": "21 січня",
            },
        }

        # filtered_tours = {}
        # for key, value in tours.items():
        #     if value["departure"] == departure:
        #         filtered_tours[key] = value
        filtered_tours = {key: value for key, value in tours.items() if value["departure"] == departure}
        return render_template("index.html", departures=departures, tours=filtered_tours)

    return render_template("index.html", title=title, departures=departures, tours=tours, cookies=request.cookies.get('cookies_name'))


@app.route('/departures/')
def departures():
    return render_template("departures.html")


@app.route('/tours/')
def list_tours():
    return render_template("tours.html")

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if not request.cookies.get('cookies_name') and request.method.post == 'POST':
        res = make_response("setting a cookies")
        res.set_cookie('username', request.form.get("name"), max_age=1 * 60 * 60 * 24 * 365)
        return res

    elif request.method == 'GET':
        return render_template("login.html")


@app.route('/cookie/')
def cookie():
    if not request.cookies.get("cookies_name") or request.cookies.get('cookies.name') == 'None':
        return redirect(url_for("login"))
    else:
        res = make_response(f"Value of cookies is {request.cookies.get('cookies_name')}")
        return res










if __name__ == '__main__':
    app.run()
