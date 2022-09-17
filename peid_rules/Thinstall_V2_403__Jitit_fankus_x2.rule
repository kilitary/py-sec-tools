rule _Thinstall_V2_403__Jitit_fankus
{
	meta:
		description = "Thinstall V2_403 __ Jitit"
	strings:
		$a = {9C60E80000000058BB????????2BC35068????????68????????68????????E8C1FEFFFFE997FFFFFFCCCC558BEC83C4F4FC5357568B75088B7D0CC745FC0800000033DBBA000000804333C0E819010000730E8B4D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
