rule _VC8__Microsoft_Corporation_vtcjts
{
	meta:
		description = "VC8 __ Microsoft Corporation"
	strings:
		$a = {E8????????E9????FFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
