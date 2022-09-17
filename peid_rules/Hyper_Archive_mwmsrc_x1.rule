rule _Hyper_Archive_mwmsrc
{
	meta:
		description = "Hyper Archive"
	strings:
		$a = {1A5354}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
