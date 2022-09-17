rule _FOXSQZ_Archive_fjubah
{
	meta:
		description = "FOXSQZ Archive"
	strings:
		$a = {464F5853515A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
