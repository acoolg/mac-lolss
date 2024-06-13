namespace SpriteKind {
    export const lol_mail = SpriteKind.create()
    export const app = SpriteKind.create()
    export const mouse = SpriteKind.create()
    export const index = SpriteKind.create()
    export const key = SpriteKind.create()
    export const not_to_show = SpriteKind.create()
    export const message = SpriteKind.create()
    export const list = SpriteKind.create()
    export const icon = SpriteKind.create()
    export const menu_bar = SpriteKind.create()
}
function 右鍵選單 () {
	
}
// page (1) = start screen
// 
// page (0) = app screen
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.createSoundEffect(WaveShape.Square, 932, 1, 255, 68, 75, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
})
function 按下一個 (app2: Sprite, 畫面編號: number) {
    if (controller.A.isPressed() && mouse2.overlapsWith(app2)) {
        page = 畫面編號
        if (page == 1) {
            scene.setBackgroundImage(assets.image`mail screen`)
            massage_demo = sprites.create(assets.image`message demo`, SpriteKind.message)
            massage_wellcome = sprites.create(assets.image`massage wellcome`, SpriteKind.message)
            sprites.destroy(mail)
            sprites.destroy(app_store)
            massage_demo.setPosition(19, 8)
            massage_wellcome.setPosition(19, 24)
            屬標圖層往上()
        }
        if (page == 2) {
            scene.setBackgroundImage(assets.image`App store`)
            serch = sprites.create(assets.image`serch`, SpriteKind.icon)
            serch.setPosition(146, 115)
            sprites.destroy(mail)
            sprites.destroy(app_store)
        }
    }
}
controller.combos.attachCombo("b, a, b, a", function () {
    初始化()
})
// page (0) = start screen
// 
// page (1) = mail
function 初始化 () {
    scene.setBackgroundImage(assets.image`準則`)
    page = 0
    mail = sprites.create(assets.image`mail`, SpriteKind.app)
    app_store = sprites.create(assets.image`appstore`, SpriteKind.app)
    mail.setPosition(19, 106)
    app_store.setPosition(36, 106)
    mouse_y = mouse2.y
    mouse_x = mouse2.x
    sprites.destroy(mouse2)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    mouse2 = sprites.create(assets.image`mouse`, SpriteKind.mouse)
    sprites.destroyAllSpritesOfKind(SpriteKind.message)
    mouse2.setPosition(mouse_x, mouse_y)
    controller.moveSprite(mouse2)
}
controller.combos.attachCombo("up, b, a", function () {
	
})
function 頁面 () {
    if (page == 1) {
        按下郵件(massage_wellcome, "歡迎使用mac lols")
    }
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.createSoundEffect(WaveShape.Noise, 3900, 4601, 255, 68, 10, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
    rename = sprites.create(assets.image`copy`, SpriteKind.menu_bar)
    rename.setPosition(mouse2.x, mouse2.y)
})
function 屬標圖層往上 () {
    mouse_y = mouse2.y
    mouse_x = mouse2.x
    sprites.destroy(mouse2)
    mouse2 = sprites.create(assets.image`mouse`, SpriteKind.mouse)
    mouse2.setPosition(mouse_x, mouse_y)
    controller.moveSprite(mouse2)
}
controller.combos.attachCombo("up, up, down, down, left, right, left, right, B, A", function () {
    if (keybord_show) {
        keybord_show = false
        sprites.destroy(keyboard)
        sprites.destroyAllSpritesOfKind(SpriteKind.key)
    } else {
        music.play(music.createSoundEffect(WaveShape.Sine, 200, 600, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
        keyboard = sprites.create(assets.image`key board`, SpriteKind.index)
        屬標圖層往上()
        keybord_show = true
        key_1 = sprites.create(assets.image`key 1`, SpriteKind.key)
        key_2 = sprites.create(assets.image`key 2`, SpriteKind.key)
        key_3 = sprites.create(assets.image`key 3`, SpriteKind.key)
        key_4 = sprites.create(assets.image`key 4`, SpriteKind.key)
        key_5 = sprites.create(assets.image`key 5`, SpriteKind.key)
        key_6 = sprites.create(assets.image`key 6`, SpriteKind.key)
        key_7 = sprites.create(assets.image`key 7`, SpriteKind.key)
        key_8 = sprites.create(assets.image`key 8`, SpriteKind.key)
        key_9 = sprites.create(assets.image`key 9`, SpriteKind.key)
        key_0 = sprites.create(assets.image`key 0`, SpriteKind.key)
        key_1.setPosition(8, 66)
        key_2.setPosition(24, 66)
        key_3.setPosition(40, 66)
        key_4.setPosition(56, 66)
        key_5.setPosition(72, 66)
        key_6.setPosition(88, 66)
        key_7.setPosition(104, 66)
        key_8.setPosition(120, 66)
        key_9.setPosition(136, 66)
        key_0.setPosition(152, 66)
    }
})
function 按下郵件 (郵件: Sprite, 訊息: string) {
    if (mouse2.overlapsWith(郵件) && controller.A.isPressed()) {
        mouse2.sayText(訊息, 5000, true)
    }
}
let key_0: Sprite = null
let key_9: Sprite = null
let key_8: Sprite = null
let key_7: Sprite = null
let key_6: Sprite = null
let key_5: Sprite = null
let key_4: Sprite = null
let key_3: Sprite = null
let key_2: Sprite = null
let key_1: Sprite = null
let keyboard: Sprite = null
let rename: Sprite = null
let mouse_x = 0
let mouse_y = 0
let serch: Sprite = null
let massage_wellcome: Sprite = null
let massage_demo: Sprite = null
let page = 0
let mouse2: Sprite = null
let keybord_show = false
let app_store: Sprite = null
let mail: Sprite = null
scene.setBackgroundImage(assets.image`準則`)
mail = sprites.create(assets.image`mail`, SpriteKind.app)
app_store = sprites.create(assets.image`appstore`, SpriteKind.app)
keybord_show = false
mail.setPosition(19, 106)
app_store.setPosition(36, 106)
mouse2 = sprites.create(assets.image`mouse`, SpriteKind.mouse)
controller.moveSprite(mouse2)
game.showLongText("這是由YT老錢大事典所做的作業系統Mac lols。由搖桿控制鼠標。A代表左鍵，B代表右鍵。上上下下左右左右ba，即可叫出鍵盤。", DialogLayout.Full)
keybord_show = false
mouse2.setStayInScreen(true)
forever(function () {
    按下一個(mail, 1)
    按下一個(app_store, 2)
    頁面()
})
