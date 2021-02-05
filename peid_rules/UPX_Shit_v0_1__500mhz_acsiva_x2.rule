rule _UPX_Shit_v0_1__500mhz_acsiva
{
	meta:
		description = "UPX_Shit v0_1 __ 500mhz"
	strings:
		$a = {E8????????5E83C6??AD89C7AD89C1AD300747E2??ADFFE0C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
