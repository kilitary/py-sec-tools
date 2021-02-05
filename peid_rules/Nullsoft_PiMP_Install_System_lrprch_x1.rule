rule _Nullsoft_PiMP_Install_System_lrprch
{
	meta:
		description = "Nullsoft PiMP Install System"
	strings:
		$a = {83EC??535556}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
