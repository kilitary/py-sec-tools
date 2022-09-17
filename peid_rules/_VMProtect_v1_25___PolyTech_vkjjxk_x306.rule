rule __VMProtect_v1_25___PolyTech_vkjjxk
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585B9D585F5E595D5D5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
