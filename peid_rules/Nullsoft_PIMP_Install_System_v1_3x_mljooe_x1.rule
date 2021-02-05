rule _Nullsoft_PIMP_Install_System_v1_3x_mljooe
{
	meta:
		description = "Nullsoft PIMP Install System v1_3x"
	strings:
		$a = {558BEC81EC????000056576A??BE????????598DBD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
