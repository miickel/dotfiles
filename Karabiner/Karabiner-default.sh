#!/bin/sh

cli=/Applications/Karabiner.app/Contents/Library/bin/karabiner

$cli set remap.doublepresscommandQ 1
/bin/echo -n .
$cli set repeat.wait 30
/bin/echo -n .
$cli set repeat.initial_wait 300
/bin/echo -n .
$cli set parameter.keyoverlaidmodifier_timeout 300
/bin/echo -n .
$cli set remap.controlL2controlL_escape 1
/bin/echo -n .
$cli set space_cadet.left_control_to_hyper 1
/bin/echo -n .
$cli set private.switch_profile 1
/bin/echo -n .
$cli set asthena.tab_to_hyper 1
/bin/echo -n .
/bin/echo
