rule _ACProtect_1_09g__Risco_software_Inc__xtjlex
{
	meta:
		description = "ACProtect 1_09g __ Risco software Inc_"
	strings:
		$a = {60F950E8010000007C58584950E8010000007E5858790466B9B872E8010000007A83C40485C8EB01EBC1F8BE72037301740F8101000000F9EB0175F9E8010000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
