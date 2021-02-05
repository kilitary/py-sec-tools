rule _UPX_Shit_v0_1__500mhz_eeykus
{
	meta:
		description = "UPX_Shit v0_1 __ 500mhz"
	strings:
		$a = {E8000000005D8BCD81ED7A29400089AD0F6D4000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
