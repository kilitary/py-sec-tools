rule _NFO_v1_x_modified_fekoye
{
	meta:
		description = "NFO v1_x modified"
	strings:
		$a = {609C8D50}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
