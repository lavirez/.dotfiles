-- Night theme: loaded via theme/current.lua (symlink managed by scripts/theme-switch)
hl.config({
    general = {
        gaps_in  = 5,
        gaps_out = 5,

        col = {
            active_border   = { colors = {"rgba(ffffffaa)", "rgba(b0b5c133)"}, angle = 135 },
            inactive_border = "rgba(ffffff22)",
        },
    },

    decoration = {
        rounding = 10,

        active_opacity   = 1,
        inactive_opacity = 0.84,

        shadow = {
            range        = 4,
            render_power = 3,
            color        = 0xee1a1a1a,
        },

        blur = {
            size     = 3,
            passes   = 1,
            vibrancy = 0.1696,
        },
    },
})
