rule _ACE_Archive_zgujws
{
	meta:
		description = "ACE Archive"
	strings:
		$a = {??????????????2A2A4143452A2A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
