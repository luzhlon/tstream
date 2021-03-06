set_project 'tstream'
-- the debug mode
if is_mode("debug") then
    -- enable the debug symbols
    set_symbols("debug")
    -- disable optimization
    set_optimize("none")
end
-- the release mode
if is_mode("release") then
    -- set the symbols visibility: hidden
    set_symbols("hidden")
    -- enable fastest optimization
    set_optimize("fastest")
    -- strip all symbols
    set_strip("all")
end

target 'test'
    set_kind 'binary'
    add_files 'test/*.cpp'
