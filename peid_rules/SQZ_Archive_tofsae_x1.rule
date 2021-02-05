rule _SQZ_Archive_tofsae
{
	meta:
		description = "SQZ Archive"
	strings:
		$a = {484C53515A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
