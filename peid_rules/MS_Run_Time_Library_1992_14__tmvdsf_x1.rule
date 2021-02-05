rule _MS_Run_Time_Library_1992_14__tmvdsf
{
	meta:
		description = "MS Run_Time Library 1992 _14_"
	strings:
		$a = {1E068CC88ED88CC0A3????83C0??A3????B430}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
