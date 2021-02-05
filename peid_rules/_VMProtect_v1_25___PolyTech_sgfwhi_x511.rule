rule __VMProtect_v1_25___PolyTech_sgfwhi
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????53525056515756559C68000000008B74242C89E581ECC000000089E70375008A060FB6C046FF2485????????8A068A040783ED026689450046E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
