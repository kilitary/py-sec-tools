rule _JRC_Archive_eypair
{
	meta:
		description = "JRC Archive"
	strings:
		$a = {4A526368697665}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
