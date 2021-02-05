rule _MetaWare_High_C_Run_Time_Library__Phar_Lap_DOS_Extender_1983_89_xqxpfi
{
	meta:
		description = "MetaWare High C Run_Time Library _ Phar Lap DOS Extender 1983_89"
	strings:
		$a = {B8????50B8????50CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
