rule _Vx_KBDflags_1024_jtooxk
{
	meta:
		description = "Vx_ KBDflags_1024"
	strings:
		$a = {8BEC2E892E2403BC00048CD52E892E22}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
