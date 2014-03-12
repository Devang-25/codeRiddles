// Floyd-Warshall algorithm
// 
//  solves the all-pairs shortest path problem using Floyd-Warshall algorithm
//  inputs:  nn, number of nodes
//           connectivity matrix cmat, where 0 means disconnected
//             and distances are all positive.  array of doubles of
//             length (nn*nn).
//  outputs: 
//           dist_mat - shortest path distances(the answer)
//           pred_mat - predicate matrix, useful in reconstructing shortest routes
//           Note that the caller should provide empty pointers as this 
//           function will handle the malloc() calls.
void fwarsh(int nn, double *cmat, double **dist_mat, int **pred_mat)
{
  double *dist;
  int *pred;
  int i,j,k; //loop counters

  //initialize data structures
  dist = (double *)malloc(sizeof(double) * nn * nn);
  pred = (int *)malloc(sizeof(int) * nn * nn);
  memset(dist, 0, sizeof(double)*nn*nn);
  memset(pred, 0, sizeof(int)*nn*nn);

  //algorithm initialization
  for (i=0; i < nn; i++) {
    for (j=0; j < nn; j++) {
      if (cmat[i*nn+j] != 0.0)
	dist[i*nn+j] = cmat[i*nn + j];
      else
	dist[i*nn+j] = HUGE_VAL; //disconnected

      if (i==j)  //diagonal case
	dist[i*nn+j] = 0;

      if ((dist[i*nn + j] > 0.0) && (dist[i*nn+j] < HUGE_VAL))
	pred[i*nn+j] = i;
    }
  }
 
  //Main loop of the algorithm
  for (k=0; k < nn; k++) {
    for (i=0; i < nn; i++) {
      for (j=0; j < nn; j++) {
	if (dist[i*nn+j] > (dist[i*nn+k] + dist[k*nn+j])) {
	  dist[i*nn+j] = dist[i*nn+k] + dist[k*nn+j];
	  pred[i*nn+j] = k; 
	  //printf("updated entry %d,%d with %d\n", i,j, dist[i*nn+j]);
	}
      }
    }
  }

  /* //Print out the results table of shortest distances
  for (i=0; i < nn; i++) {
    for (j=0; j < nn; j++)
      printf("%g ", dist[i*nn+j]);
    printf("\n");
    } */
  
  //now set the dist and pred matrices for the calling function
  //but do some checks because we allow NULL to be passed if the user
  //doesn't care about one of the results.
  if (dist_mat)
    *dist_mat = dist;
  else
    free(dist);

  if (pred_mat)
    *pred_mat = pred;
  else
    free(pred);

  return;
