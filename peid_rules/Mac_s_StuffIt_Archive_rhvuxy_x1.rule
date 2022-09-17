rule _Mac_s_StuffIt_Archive_rhvuxy
{
	meta:
		description = "Mac_s StuffIt Archive"
	strings:
		$a = {5349542100}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
