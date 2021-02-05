rule _WARNING__TROJAN__HuiGeZi_puvswj
{
	meta:
		description = "WARNING __ TROJAN __ HuiGeZi"
	strings:
		$a = {558BEC81C4??FEFFFF53565733C08985??FEFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
