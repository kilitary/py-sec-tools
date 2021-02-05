rule _Nullsoft_PiMP_Install_System_v1_x_fvmvhq
{
	meta:
		description = "Nullsoft PiMP Install System v1_x"
	strings:
		$a = {83EC5C53555657FF15??????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
