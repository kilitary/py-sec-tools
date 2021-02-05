rule _Anti007__NsPacK_Private_qhuhhh
{
	meta:
		description = "Anti007 __ NsPacK Private"
	strings:
		$a = {000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000????????????????????????0010000000000000????????00000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
