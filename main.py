@namespace
class SpriteKind:
    lol_mail = SpriteKind.create()
    app = SpriteKind.create()
    mouse = SpriteKind.create()
    index = SpriteKind.create()
    key = SpriteKind.create()
    not_to_show = SpriteKind.create()
    message = SpriteKind.create()
# page (1) = start screen
# 
# page (0) = app screen

def on_a_pressed():
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            932,
            1,
            255,
            68,
            75,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def 按下一個(app2: Sprite, 畫面編號: number):
    global page, massage_demo, massage_wellcome, serch
    if controller.A.is_pressed() and mouse2.overlaps_with(app2):
        page = 畫面編號
        if page == 1:
            scene.set_background_image(assets.image("""
                mail screen
            """))
            massage_demo = sprites.create(assets.image("""
                message demo
            """), SpriteKind.message)
            massage_wellcome = sprites.create(assets.image("""
                    massage wellcome
                """),
                SpriteKind.message)
            sprites.destroy(mail)
            sprites.destroy(app_store)
            massage_demo.set_position(19, 8)
            massage_wellcome.set_position(19, 24)
            屬標圖層往上()
        if page == 2:
            scene.set_background_image(assets.image("""
                App store
            """))
            serch = sprites.create(assets.image("""
                serch
            """), SpriteKind.player)
            serch.set_position(146, 115)
            sprites.destroy(mail)
            sprites.destroy(app_store)

def on_combos_attach_combo():
    初始化()
controller.combos.attach_combo("b, a, b, a", on_combos_attach_combo)

# page (0) = start screen
# 
# page (1) = mail
def 初始化():
    global page, mail, app_store, mouse_y, mouse_x, mouse2
    scene.set_background_image(assets.image("""
        準則
    """))
    page = 0
    mail = sprites.create(assets.image("""
        mail
    """), SpriteKind.app)
    app_store = sprites.create(assets.image("""
        appstore
    """), SpriteKind.app)
    mail.set_position(19, 106)
    app_store.set_position(36, 106)
    mouse_y = mouse2.y
    mouse_x = mouse2.x
    sprites.destroy(mouse2)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    mouse2 = sprites.create(assets.image("""
        mouse
    """), SpriteKind.mouse)
    sprites.destroy_all_sprites_of_kind(SpriteKind.message)
    mouse2.set_position(mouse_x, mouse_y)
    controller.move_sprite(mouse2)

def on_combos_attach_combo2():
    pass
controller.combos.attach_combo("up, b, a", on_combos_attach_combo2)

def 頁面():
    if page == 1:
        按下郵件(massage_wellcome, "歡迎使用mac lols")

def on_b_pressed():
    music.play(music.create_sound_effect(WaveShape.NOISE,
            3900,
            4601,
            255,
            68,
            10,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def 屬標圖層往上():
    global mouse_y, mouse_x, mouse2
    mouse_y = mouse2.y
    mouse_x = mouse2.x
    sprites.destroy(mouse2)
    mouse2 = sprites.create(assets.image("""
        mouse
    """), SpriteKind.mouse)
    mouse2.set_position(mouse_x, mouse_y)
    controller.move_sprite(mouse2)

def on_combos_attach_combo3():
    global keybord_show, keyboard, key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_0
    if keybord_show:
        keybord_show = False
        sprites.destroy(keyboard)
        sprites.destroy_all_sprites_of_kind(SpriteKind.key)
    else:
        music.play(music.create_sound_effect(WaveShape.SINE,
                200,
                600,
                255,
                0,
                150,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
        keyboard = sprites.create(assets.image("""
            key board
        """), SpriteKind.index)
        屬標圖層往上()
        keybord_show = True
        key_1 = sprites.create(assets.image("""
            key 1
        """), SpriteKind.key)
        key_2 = sprites.create(assets.image("""
            key 2
        """), SpriteKind.key)
        key_3 = sprites.create(assets.image("""
            key 3
        """), SpriteKind.key)
        key_4 = sprites.create(assets.image("""
            key 4
        """), SpriteKind.key)
        key_5 = sprites.create(assets.image("""
            key 5
        """), SpriteKind.key)
        key_6 = sprites.create(assets.image("""
            key 6
        """), SpriteKind.key)
        key_7 = sprites.create(assets.image("""
            key 7
        """), SpriteKind.key)
        key_8 = sprites.create(assets.image("""
            key 8
        """), SpriteKind.key)
        key_9 = sprites.create(assets.image("""
            key 9
        """), SpriteKind.key)
        key_0 = sprites.create(assets.image("""
            key 0
        """), SpriteKind.key)
        key_1.set_position(8, 66)
        key_2.set_position(24, 66)
        key_3.set_position(40, 66)
        key_4.set_position(56, 66)
        key_5.set_position(72, 66)
        key_6.set_position(88, 66)
        key_7.set_position(104, 66)
        key_8.set_position(120, 66)
        key_9.set_position(136, 66)
        key_0.set_position(152, 66)
controller.combos.attach_combo("up, up, down, down, left, right, left, right, B, A",
    on_combos_attach_combo3)

def 按下郵件(郵件: Sprite, 訊息: str):
    if mouse2.overlaps_with(郵件) and controller.A.is_pressed():
        mouse2.say_text(訊息, 5000, True)
key_0: Sprite = None
key_9: Sprite = None
key_8: Sprite = None
key_7: Sprite = None
key_6: Sprite = None
key_5: Sprite = None
key_4: Sprite = None
key_3: Sprite = None
key_2: Sprite = None
key_1: Sprite = None
keyboard: Sprite = None
mouse_x = 0
mouse_y = 0
serch: Sprite = None
massage_wellcome: Sprite = None
massage_demo: Sprite = None
page = 0
mouse2: Sprite = None
keybord_show = False
app_store: Sprite = None
mail: Sprite = None
scene.set_background_image(assets.image("""
    準則
"""))
mail = sprites.create(assets.image("""
    mail
"""), SpriteKind.app)
app_store = sprites.create(assets.image("""
    appstore
"""), SpriteKind.app)
keybord_show = False
mail.set_position(19, 106)
app_store.set_position(36, 106)
mouse2 = sprites.create(assets.image("""
    mouse
"""), SpriteKind.mouse)
controller.move_sprite(mouse2)
game.show_long_text("這是由YT老錢大事典所做的作業系統Mac lols。由搖桿控制鼠標。A代表左鍵，B代表右鍵。上上下下左右左右ba，即可叫出鍵盤。",
    DialogLayout.FULL)
keybord_show = False
mouse2.set_stay_in_screen(True)

def on_forever():
    按下一個(mail, 1)
    按下一個(app_store, 2)
    頁面()
forever(on_forever)
