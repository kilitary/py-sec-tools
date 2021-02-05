rule _Dr_Web_Virus_Finding_Engine__InSoft_EDV_Systeme_zawmpc
{
	meta:
		description = "Dr_Web Virus_Finding Engine __ InSoft EDV_Systeme"
	strings:
		$a = {2CE8????????5D8BC581EDF673????2B85????????83E8068985}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
