rule _MS_Run_Time_Library_1990_1992_09__msbbqd
{
	meta:
		description = "MS Run_Time Library 1990_ 1992 _09_"
	strings:
		$a = {B430CD213C0273??C38CDF8B36????2E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
