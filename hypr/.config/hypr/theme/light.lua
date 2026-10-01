-- Day theme: loaded via theme/current.lua (symlink managed by scripts/theme-switch)
hl.config({
    general = {
        gaps_in  = 6,
        gaps_out = 10,

        col = {
            active_border   = { colors = {"rgba(3a3f4bcc)", "rgba(8a93a666)"}, angle = 135 },
            inactive_border = "rgba(1a1d2322)",
        },
    },

    decoration = {
        rounding = 12,

        active_opacity   = 1,
        inactive_opacity = 0.95,

        shadow = {
            range        = 12,
            render_power = 3,
            color        = 0x33000000,
        },

        blur = {
            size     = 3,
            passes   = 2,
            vibrancy = 0.1696,
        },
    },
})
