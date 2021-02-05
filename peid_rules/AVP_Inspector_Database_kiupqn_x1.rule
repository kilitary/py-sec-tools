rule _AVP_Inspector_Database_kiupqn
{
	meta:
		description = "AVP Inspector Database"
	strings:
		$a = {47686F737420427573746572}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
