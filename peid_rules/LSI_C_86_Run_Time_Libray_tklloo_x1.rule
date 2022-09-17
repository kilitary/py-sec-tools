rule _LSI_C_86_Run_Time_Libray_tklloo
{
	meta:
		description = "LSI C_86 Run_Time Libray"
	strings:
		$a = {B8????8EC00617BC????268C??????B430CD2126A3????FC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
