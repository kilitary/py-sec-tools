rule _ACE_SFX_Archive_boriqu
{
	meta:
		description = "ACE_SFX Archive"
	strings:
		$a = {2A2A4143452A2A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
