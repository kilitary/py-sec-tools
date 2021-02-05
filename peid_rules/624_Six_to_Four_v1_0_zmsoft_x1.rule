rule _624_Six_to_Four_v1_0_zmsoft
{
	meta:
		description = "624 _Six to Four_ v1_0"
	strings:
		$a = {50554C5083????FCBF????BE????B5??57F3A5C333ED}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
