rule _Program_Protector_XP_v1_0_ngarym
{
	meta:
		description = "Program Protector XP v1_0"
	strings:
		$a = {E8????????000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
